import org.junit.jupiter.api.Test;
import seminars.fourth.book.Book;
import seminars.fourth.book.BookRepository;
import seminars.fourth.book.BookService;

import java.util.List;

import static org.mockito.Mockito.mock;

public class BookTest {
    @Test
    void serviceTest(){

        BookRepository testRep = mock(BookRepository.class);
        BookService testService = new BookService(testRep);

        Book bookById = testService.findBookById("1");
        List<Book> allBooks = testService.findAllBooks();

    }
}
