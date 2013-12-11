package generator.python
import predef._

object function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function) extends base.Printer
    {
        if (args.length != 2)
            throw new Exception(s"Annotation $name should have 2 arguments in" +
                    " form (category, label_template)" + "\r\n" + "In function " + f)

        val category = args(0)
        val label_tmpl = args(1)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        type Parameter = function.Parameter
        val name = f.name
        val alias = name

        def bind = Def("bind", "ctx", "self._ctx = ctx.clone()")

        def reset = Def("reset", "",
            "self.impl = self.getImpl()" |
            "ctx = getattr(self, '_ctx', None)" |
            "if ctx: context.bind(self.impl, ctx)") |||
            ImportFrom("context", "marketsim")

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override val base_class : Code = "Function[float]" |||
                                            ImportFrom("Function", "marketsim.ops._function")

        override def init_body =
            super.init_body |
            "self.impl = self.getImpl()"

        override def call_body = "return self.impl()"

        override def body = super.body | internals | attributes | getImpl | bind | reset | call

        def getImpl = Def("getImpl", "", "return " + f.body.get.asPython) ||| Code.from(f.body.get.imports)

        def internals = "_internals = ['impl']"

        def attributes = Prop("attributes", "return {}")
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.function"
}