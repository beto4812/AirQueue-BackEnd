import jess.Rete;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;

public class BaseServlet extends HttpServlet {


    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        doGet(request, response);
    }

    protected void checkInitialized() throws ServletException {
        ServletContext servletContext = getServletContext();
        String rulesFile = servletContext.getInitParameter("rulesfile");
        String factsFile = servletContext.getInitParameter("factsfile");
        if (servletContext.getAttribute("engine") == null) {
            try {
                Rete engine = new Rete(this);
                engine.executeCommand("(batch \"" + rulesFile + "\")");
                engine.reset();
                if (new File(factsFile).exists())
                    engine.executeCommand("(load-facts \"" + factsFile + "\")");
                servletContext.setAttribute("engine", engine);
            } catch (Exception je) {
                throw new ServletException(je);
            }
        }
    }

    protected void dispatch(HttpServletRequest request,
                            HttpServletResponse response,
                            String page)
            throws IOException, ServletException {

        ServletContext servletContext = getServletContext();
        RequestDispatcher dispatcher =
                servletContext.getRequestDispatcher(page);
        dispatcher.forward(request, response);
    }
}
