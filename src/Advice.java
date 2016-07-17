
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

        int age = -1, sensitivity = -1, airQualityIndex = -1;
        try {
            age = Integer.parseInt(request.getParameter("age"));
            sensitivity = Integer.parseInt(request.getParameter("sensitivity"));
            airQualityIndex = Integer.parseInt(request.getParameter("airQualityIndex"));
        } catch (Exception e) {

        }
        String resp = "{\"response\": ";
        //response.getWriter().println("age: " + age + " sensitivity: " + sensitivity);

        if (age != -1 && sensitivity != -1 && airQualityIndex != -1) {
            Rete engine = (Rete) servletContext.getAttribute("engine");

            try {
                //engine.executeCommand("(assert (clean-up-order 1))");
                Value airQualityIndexValue = new Value(airQualityIndex, RU.INTEGER);
                Fact pollutionLevel = new Fact("pollutionLevel", engine);
                pollutionLevel.setSlotValue("value", airQualityIndexValue);


                Value ageValue = new Value(age, RU.INTEGER);
                Value sensitivityValue = new Value(sensitivity, RU.INTEGER);
                Fact person = new Fact("person", engine);
                person.setSlotValue("age", ageValue);
                person.setSlotValue("sensitivity", sensitivityValue);

                engine.assertFact(pollutionLevel);
                engine.assertFact(person);
                engine.run();

                Iterator result =
                        engine.runQuery("all-advices", new ValueVector());

                //ArrayList<Fact> facts = new ArrayList<>();

                while (result.hasNext()) {
                    jess.Token token = (jess.Token) result.next();
                    //response.getWriter().println("token size: " + token.size());
                    for(int i = 1; i<=token.size(); i++){
                        //facts.add(token.fact(i));
                        engine.retract(token.fact(i));
                    }
                    Fact advice = token.topFact();
                    resp += "{\"advice\": {";
                    String adviceText = ((jess.Value) advice.getSlotValue("text")).toString();
                    resp += "\"text\": " + adviceText + ",";
                    String level = ((jess.Value) advice.getSlotValue("level")).toString();
                    resp += "\"level\": " + level;
                }
                resp += "}}";
                engine.run();

            } catch (Exception e) {
                response.getWriter().println(e);
                throw new ServletException(e);
            }
            resp+="}";
        } else {
            resp += "missing/invalid parameters}";
        }
        response.getWriter().println(resp);
    }
}