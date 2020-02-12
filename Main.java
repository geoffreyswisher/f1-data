import javafx.scene.Scene;
import javafx.scene.chart.PieChart;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.*;
import javafx.application.*;
import javafx.collections.*;


public class Main extends Application {

    public static void main (String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        
        TextField textfield = new TextField("Intial text");

        VBox root = new VBox();
        root.setSpacing(100);
        root.setPadding(new Insets(20,10,20,10));

        HBox wrapper = new HBox();
        wrapper.setAlignment(Pos.CENTER);

        HBox hbox = new HBox();
        hbox.setSpacing(100);
        hbox.setAlignment(Pos.CENTER);

        Label label = new Label("n/a");

        EventHandler<ActionEvent> event = new EventHandler<ActionEvent>() {
            public void handle(ActionEvent e) {
                label.setText(textfield.getText());
            }
        };

        textfield.setOnAction(event);

        ObservableList<PieChart.Data> pieChartData = 
            FXCollections.observableArrayList(
                new PieChart.Data("name", 5),
                new PieChart.Data("namee", 6)
            );
        
        final PieChart chart = new PieChart(pieChartData);

        hbox.getChildren().add(label);
        hbox.getChildren().add(textfield);

        wrapper.getChildren().add(chart);

        root.getChildren().add(hbox);
        root.getChildren().add(wrapper);

        Scene scene = new Scene(root, 750, 1000);

        primaryStage.setTitle("F1 Data Analysis");
        primaryStage.setScene(scene);
        primaryStage.show();

    }
    
}