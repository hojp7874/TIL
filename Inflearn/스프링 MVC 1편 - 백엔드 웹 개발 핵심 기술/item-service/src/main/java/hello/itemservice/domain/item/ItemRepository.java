package hello.itemservice.domain.item;

import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Repository
public class ItemRepository {

    // HashMap, long 쓰면 안됨. 동시에 접근할 때 데이터가 겹칠 수 있음.
    // static: 객체 생성될 때마다 새로 선언되지 않게 하려고
    private static final Map<Long, Item> store = new HashMap<>();
    private static long sequence = 0L;

    public Item save(Item item) {
        item.setId(++sequence);
        store.put(item.getId(), item);
        return item;
    }

    public Item findById(Long id) {
        return store.get(id);
    }

    public List<Item> findAll() {
        return new ArrayList<>(store.values());
    }

    // 정석은 id가 없는 객체를 따로 만들어 그걸 input으로 받아야 함.
    public void update(Long id, Item updateParam) {
        updateParam.setId(id);
        store.put(updateParam.getId(), updateParam);
    }

    public void clearStore() {
        store.clear();
    }
}
