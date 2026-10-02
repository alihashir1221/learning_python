#Install an external module and import it into your program. Use the module to perform a task of your choice. Write a brief description of what the module does and how you used it in your program.
#pyttsx3 is a text-to-speech conversion library in Python. It allows you to convert text into spoken words, making it useful for applications that require audio output. In this program, I used the pyttsx3 module to read aloud a given text input.
import pyttsx3
engine = pyttsx3.init()



engine.say("Let's learn Python programming together! Python is a versatile and powerful programming language that is widely used in various fields, including web development, data analysis, artificial intelligence, and more. By learning Python, you can enhance your coding skills and open up new opportunities in the tech industry.")
engine.runAndWait()