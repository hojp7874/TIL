package hello.servlet.basic;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "helloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        System.out.println("HelloServlet.service");
        System.out.println("req = " + req);
        System.out.println("resp = " + resp);

        String username = req.getParameter("username"); //req.getParameter 메서드로 간편히 데이터를 가져올 수 있다.
        System.out.println("username = " + username);

        resp.setContentType("text/plain"); //컨텐츠타입 입력
        resp.setCharacterEncoding("utf-8"); //인코딩 타입 입력. 요즘은 다 utf-8을 쓴다
        resp.getWriter().write("hello " + username); //페이지 소스에 전송할 데이터 입력

    }
}
