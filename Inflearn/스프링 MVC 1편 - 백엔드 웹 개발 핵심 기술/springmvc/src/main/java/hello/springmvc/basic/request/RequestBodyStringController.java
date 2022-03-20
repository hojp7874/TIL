package hello.springmvc.basic.request;

import lombok.extern.slf4j.Slf4j;
import org.springframework.http.*;
import org.springframework.stereotype.Controller;
import org.springframework.util.StreamUtils;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.ServletInputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.Writer;
import java.lang.reflect.Type;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

@Slf4j
@Controller
public class RequestBodyStringController {

    @PostMapping("/request-body-string-v1")
    public void requestBodyString(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        ServletInputStream inputStream = req.getInputStream();
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);

        log.info("messageBody={}", messageBody);
        resp.getWriter().write("ok");
    }

    @PostMapping("/request-body-string-v2")
    public void requestBodyStringV2(InputStream inputStream, Writer responseWriter) throws IOException {

        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);
        log.info("messageBody={}", messageBody);
        responseWriter.write("ok");
    }

    @PostMapping("/request-body-string-v3")
    public HttpEntity<String> requestBodyStringV3(HttpEntity<String> httpEntity) {

        String messageBody = httpEntity.getBody();
        HttpHeaders headers = httpEntity.getHeaders();
        log.info("messageBody={}", messageBody);
        log.info("headers={}", headers);
        return new HttpEntity<>("ok");
    }

    @PostMapping("/request-body-string-v3-2")
    public HttpEntity<String> requestBodyStringV32(RequestEntity<String> httpEntity) {

        String messageBody = httpEntity.getBody();
        HttpHeaders headers = httpEntity.getHeaders();
        HttpMethod method = httpEntity.getMethod();
        URI url = httpEntity.getUrl();
        Type type = httpEntity.getType();
        log.info("messageBody={}", messageBody);
        log.info("headers={}", headers);
        log.info("method={}", method);
        log.info("url={}", url);
        log.info("type={}", type);
        return new ResponseEntity<String>("ok", HttpStatus.CREATED);
    }

    @ResponseBody
    @PostMapping("/request-body-string-v4")
    public String requestBodyStringV4(@RequestBody String messageBody, @RequestHeader Map<String, String> headers) {

        log.info("messageBody={}", messageBody);
        log.info(headers.toString());
        return "ok";
    }
}
