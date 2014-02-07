package generator.python

import java.io._
import resource._
import scala.Some

package object gen
{
    // TODO: memoization
    def generationUnit(f : Typed.Function) = 
    {
        if (f.tryGetAttribute("python") == Some("no"))
            None
        else
            f.annotations collect {
                case Typed.Annotation(g : PythonGenerator, args) => g.generatePython(args)_
            } match {
                case Nil =>
                    Some(base.python.generatePython(Nil)(f))

                case g :: Nil =>
                    Some(g(f))

                case _ => throw new Exception("Multiple python generators are given for function " + f)
            }
    }
    
    def apply(p : Typed.Package, dst_dir : String, idx_dir : String)
    {
        apply(p, new File(dst_dir), new File(idx_dir))
    }

    def apply(p : Typed.Package, dir : File, idx_dir : File)
    {
        ensure_dir(dir)
        ensure_dir(idx_dir)

        p.packages.values foreach { sub => apply(sub, new File(dir, sub.name), new File(idx_dir, sub.name) ) }

        def printWriter(dst_dir : File, filename : String) =
            new PrintWriter(
                new BufferedWriter(
                    new OutputStreamWriter(
                        new FileOutputStream(
                            new File(dst_dir, filename), true))),
            true)

        if (config.verbose)
            println("\t" + p.qualifiedName)

        for (idx_out <- managed(printWriter(idx_dir, "__init__.py")))
        {
            p.functions.values foreach { _ foreach {
                case f : Typed.Function =>
                    try {
                        generationUnit(f) map { g =>
                            //println(f.parent.qualifiedName, f.name)
                            for (out <- managed(printWriter(dir, s"_${f.name}.py"))) {
                                out.println(g.code)

                                if (f.name != g.name &&
                                        (!f.qualifiedName.names.contains("orderbook") ||
                                                List("Local").exists({ n => f.qualifiedName.names.contains(n)}))) {
                                    import predef._
                                    val input_args = f.parameters map { _.name + " = None" } mkString ","
                                    val args_to_pass = f.parameters map { _.name } mkString ","

                                    def typecheck(args : List[Typed.Parameter]) : Code = args match {
                                        case Nil =>
                                            s"return ${g.name}($args_to_pass)"
                                        case x :: tl =>
                                            (s"if ${x.name} is None or rtti.can_be_casted(${x.name}, " ||| x.ty.asCode ||| "):"
                                                |> typecheck(tl))
                                    }

                                    val resolver =
                                        s"def ${f.name}($input_args): " |> base.withImports(
                                                typecheck(f.parameters) |||
                                                ImportFrom("rtti", "marketsim") |
                                                """raise Exception("Cannot find suitable overload")""")

                                    out.println(resolver)
                                }
                                else
                                    out.println(f.name + " = " + g.name)
                            }
                            idx_out.println(base.withImports(Printer.importsOf(f)))
                        }
                    } catch {
                        case e : Exception =>
                            if (config.catch_errors) {
                                println(s"An exception '${e.getMessage}' caught when generating python code for $f")
                                println(e.getMessage)
                            }
                    }
                case f : Typed.FunctionAlias =>
                    generationUnit(f.target) map { g =>
                        idx_out.println(base.withImports(Printer.importsOf(f.target).as(f.name)))
                    }
            } }

            if (p.types.nonEmpty)
            {
                for (out <- managed(printWriter(dir, "_types.py")))
                {
                    p.types.values foreach {
                        case interface : Typed.InterfaceDecl =>
                            if (interface.generics.isEmpty) {
                                val name = interface.name
                                val bases = interface.bases map { "," + _.toString } mkString ""
                                out.println(s"#class $name(object$bases): pass")
                            }

                        case alias : Typed.AliasDecl =>
                            if (alias.generics.isEmpty)
                                out.println("#" + alias.name + " = " + alias.target.toString)
                    }
                }
            }

            p.packages.values foreach { pkg =>
                idx_out.println(s"import " + pkg.name)
            }

            for (out <- managed(printWriter(dir, "__init__.py"))) {}

        }

    }


    def ensure_dir(dir: File) {
        if (!dir.exists()) {
            dir.mkdirs()
            if (!dir.exists())
                throw new Exception("cannot create directory " + dir.getName)
        }
    }

    trait GenerationUnit
    {
        def name : String
        def code : predef.Code
    }

    trait PythonGenerator extends Typed.AnnotationHandler
    {
        def generatePython(/** arguments of the annotation */ args  : List[String])
                          (/** function to process         */ f     : Typed.Function) : GenerationUnit
    }

    object Annotations {

        import Typed.Annotations._

        override def toString = registry.toString()

        // TODO: non-intrusive registration
        register(random)
        register(mathops)
        register(curried)
        register(curried.after_typing)
        register(base.python)
        register(observable)
        register(function)
        register(intrinsic)
        register(intrinsic_function)
        register(intrinsic_observable)
        register(order_factory)
        register(order_factory_curried)
        register(order_factory_on_proto)
    }
}
