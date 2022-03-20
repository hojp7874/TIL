package hello.itemservice.domain.item;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

//@Data // 핵심 도메인 모델에 사용하기에는 위험하다. 그냥 데이터 왔다갔다만 하는 DTO정도만 쓰는걸 권장 (그것도 확인해보고)
@Getter @Setter
public class Item {

    private Long id;
    private String itemName;
    private Integer price;
    private Integer quantity;

    public Item() {
    }

    public Item(String itemName, Integer price, Integer quantity) {
        this.itemName = itemName;
        this.price = price;
        this.quantity = quantity;
    }
}
