import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/*
 * Name: Zain Tahir     
 * Student number: C1308094
 */

/*
 * A command-line application that pre-evaluates messages to be shortened and prints some statistics.
 */
public class EvaluatorUtility {
    public static void main(String[]args) throws FileNotFoundException{
        Evaluator sh = new Evaluator();
        String finalMessage = sh.evaluateMessage(args[0]);
        System.out.println(finalMessage);
    }
}