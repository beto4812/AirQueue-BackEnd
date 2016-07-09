
import jess.*;
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.Iterator;

public class Recommend extends BaseServlet {

    public void doGet(HttpServletRequest request,
                      HttpServletResponse response)
            throws IOException, ServletException {
        checkInitialized();

        ServletContext servletContext = getServletContext();

        String param1 = request.getParameter("param1");

        response.getWriter().println("ola: " + param1);

        Rete engine = (Rete) servletContext.getAttribute("engine");

        try{
            engine.executeCommand("(assert (clean-up-order 1))");
            engine.run();
            Iterator result =
                    engine.runQuery("all-products", new ValueVector());
            request.setAttribute("queryResult", result);
        }catch (Exception e){
            throw new ServletException(e);
        }

        /*
        try {
            Rete engine = (Rete) servletContext.getAttribute("engine");

            engine.executeCommand("(assert (clean-up-order " +
                                  orderNumberString + "))");
            engine.run();

            int orderNumber = Integer.parseInt(orderNumberString);
            Value orderNumberValue = new Value(orderNumber, RU.INTEGER);
            Value customerIdValue = new Value(customerIdString, RU.ATOM);
            Fact order = new Fact("order", engine);
            order.setSlotValue("order-number", orderNumberValue);
            order.setSlotValue("customer-id", customerIdValue);
            engine.assertFact(order);

            for (int i=0; i<items.length; ++i) {
                Fact item = new Fact("line-item", engine);
                item.setSlotValue("order-number", orderNumberValue);
                item.setSlotValue("part-number", new Value(items[i], RU.ATOM));
                item.setSlotValue("customer-id", customerIdValue);
                engine.assertFact(item);
            }
            engine.run();
            Iterator result =
                engine.runQuery("recommendations-for-order",
                                new ValueVector().add(orderNumberValue));

            if (result.hasNext()) {
                request.setAttribute("queryResult", result);
                dispatch(request, response, "/recommend.jsp");
            } else
                dispatch(request, response, "/purchase");

        } catch (JessException je) {
            throw new ServletException(je);
        }
        */
    }
}