package hello.itemservice;

import hello.itemservice.web.validation.ItemValidator;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.validation.Validator;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class ItemServiceApplication implements WebMvcConfigurer {

	public static void main(String[] args) {
		SpringApplication.run(ItemServiceApplication.class, args);
	}

	// global설정은 거의 할 일이 없다. 왜냐하면...
	// spring validator 의존성을 추가하면 자동으로 global validator로 등록되기 때문.
	// global설정을 직접 하게되면 spring validator를 못찾는다.
//	@Override
//	public Validator getValidator() {
//		return new ItemValidator();
//	}
}
