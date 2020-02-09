import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.TilePane;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.application.Application;
import javafx.collections.ObservableList;

public class Main extends Application {

    //Button button;
    TextField textfield;

    public static void main (String[] args) {
        launch(args);
    }


    @Override
    public void start(Stage primaryStage) throws Exception {
        
        textfield = new TextField("Intial text");

        StackPane root = new StackPane();
        TilePane tile = new TilePane();

        Label label = new Label("n/a");

        EventHandler<ActionEvent> event = new EventHandler<ActionEvent>() {
            public void handle(ActionEvent e) {
                label.setText(textfield.getText());
            }
        };

        textfield.setOnAction(event);

        tile.getChildren().add(label);
        tile.getChildren().add(textfield);

        root.getChildren().add(tile);

        Scene scene = new Scene(root, 500, 500);
        primaryStage.setTitle("Title");
        primaryStage.setScene(scene);
        primaryStage.show();

    }
    
}