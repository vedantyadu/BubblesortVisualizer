import tkinter as tk
import random
import threading
import time


class Column:
    def __init__(self, size, col, win):
        self.col = col
        self.size = size
        self.column = [
            tk.Label(win,width=4, height=2, bg="white")
            for i in range(0, size)
        ]
        for i in range(0, size):
            self.column[i].grid(row=i, column=col, padx=1)
    
    # Change the color of the column to a given height
    def color(self, height, color):
        for i in range(self.size - height, self.size):
            self.column[i].config(bg=color)
        
        for i in range(0, self.size - height):
            self.column[i].config(bg="white")


class BubbleSorter:
    def __init__(self, rows, cols, stopTime):
        self.win = tk.Tk()
        self.win.title("Bubblesort visualizer")
        self.rows = rows
        self.cols = cols
        self.running = False
        self.stopTime = stopTime
        
        self.columns = [
            Column(rows, i, self.win)
            for i in range(0, cols)
        ]
        
        self.arr = []

        gen = tk.Button(self.win, text='Start', width=4, command=self.start, relief='flat', bg='white')
        gen.grid(row=rows, column=0, columnspan=2, sticky='news', padx=2, pady=2)
        
        self.win.mainloop()

    # Change the color of a column from self.columns
    def color_col(self, col, height, color):
        self.columns[col].color(height, color)
    
    # Create an array of random integers and start sorting
    def start(self):
        if not self.running:
            self.arr = [random.randint(0, self.rows) for i in range(0, self.cols)]
            
            for i in range(0, self.cols):
                self.color_col(i, self.arr[i], "purple3")
            
            self.running = True
            
            thread = threading.Thread(target=self.sort)
            thread.start()
        
    # Bubblesort
    def sort(self):
        for i in range(0, self.cols):
            for j in range(0, self.cols - i - 1):
                
                # Refresh the color of all the columns
                for k in range(0, self.cols - i):
                    self.color_col(k, self.arr[k], "purple3")
                
                # Change the color of the columns currently being compared
                self.color_col(j, self.arr[j], "navy")
                self.color_col(j + 1, self.arr[j + 1], "navy")
                
                time.sleep(self.stopTime)
                
                # Swap
                if self.arr[j] > self.arr[j + 1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j + 1]
                    self.arr[j + 1] = temp

                    # Refresh the color of the columns if swapped
                    self.color_col(j, self.arr[j], "navy")
                    self.color_col(j + 1, self.arr[j + 1], "navy")

                time.sleep(self.stopTime)

            # Change the color of the sorted element(column) to "light green"
            self.color_col(self.cols - i - 1, self.arr[self.cols - i - 1], "light green")

        self.running = False
        
