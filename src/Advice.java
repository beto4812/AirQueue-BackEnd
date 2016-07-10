
import jess.*;
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.Iterator;

public class Advice extends BaseServlet {

    public void doGet(HttpServletRequest request,
                      HttpServletResponse response)
            throws IOException, ServletException {
        checkInitialized();

        ServletContext servletContext = getServletContext();

        String param1 = request.getParameter("param1");

        response.getWriter().println("ola4: " + param1);

        Rete engine = (Rete) servletContext.getAttribute("engine");

        try{
            //engine.executeCommand("(assert (clean-up-order 1))");
            Value value = new Value(1, RU.INTEGER);
            Fact pollutionLevel = new Fact("pollutionLevel", engine);
            pollutionLevel.setSlotValue("value", value);
            engine.assertFact(pollutionLevel);
            engine.run();

            Iterator result =
                    engine.runQuery("all-advices", new ValueVector());

            String s = "base: ";

            while(result.hasNext()){
                s+= result.next();
            }

            response.getWriter().println(s);


        }catch (Exception e){
            response.getWriter().println(e);
            throw new ServletException(e);
        }
    }
}