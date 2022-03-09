package hello.servlet.basic.resposnse;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "responseHeaderServlet", urlPatterns = "/response-header")
public class ResponseHeaderServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // [status-line]
        resp.setStatus(HttpServletResponse.SC_OK);

        // [response-headers]
        resp.setHeader("Content-type", "text/plain;charset=utf-8"); // charset utf-8 안하면 한글 깨질 수 있음
        resp.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");
        resp.setHeader("Pragma", "no-cache");
        resp.setHeader("my-header", "hello");

        // [Header 편의 메서드]
//        content(resp);
//        coocke(resp);
        redirect(resp);

        PrintWriter writer = resp.getWriter();
        writer.println("안녕하세요");
    }

    private void redirect(HttpServletResponse resp) throws IOException {
        // Status Code 302
        // Location: /basic/hello-form.html

//        resp.setStatus(HttpServletResponse.SC_FOUND); // 302
//        resp.setHeader("Location", "/basic/hello-form.html");
        resp.sendRedirect("/basic/hello-form.html");
    }

    private void coocke(HttpServletResponse resp) {
        // Set-Cookie: myCookie=good; Max-Age=600;
        // resp.setHeader("Set-Cookie", "myCookie=good; Max-Age=600");
        Cookie cookie = new Cookie("myCookie", "good");
        cookie.setMaxAge(600); // 600ch
        resp.addCookie(cookie);
    }

    private void content(HttpServletResponse resp) {
        // Content-Type: text/plain;charset=utf-8
        // Content-Length: 16    "안녕하세요\n" 에서 한글은 3글자, \n은 1글자 취급을 받아 16글자
        resp.setContentType("text/plain");
        resp.setCharacterEncoding("utf-8");
        // resp.setContentLength(16);    (생략시 자동 생성)
    }
}
