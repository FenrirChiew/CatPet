import random
import tkinter as tk
from tkinter import messagebox as msg


class Cat(tk.Tk):
    def __init__(self):
        super().__init__()

        # variables
        self.messagebox = None
        self.x = self.winfo_screenwidth() // 2 - 50
        self.y = self.winfo_screenheight() - self.winfo_screenheight() // 6
        self.cycle = 0
        self.check = 1
        self.event_number = random.randrange(1, 3, 1)
        path = 'CatPet\cat_gif\\'

        # right click menu
        def idle():
            msg.showerror(title="Null Action", message="This action is still unvailable.")

        def idle_to_sleep():
            msg.showerror(title="Null Action", message="This action is still unvailable.")

        def sleep():
            msg.showerror(title="Null Action", message="This action is still unvailable.")

        def sleep_to_idle():
            msg.showerror(title="Null Action", message="This action is still unvailable.")

        def walk_left():
            msg.showerror(title="Null Action", message="This action is still unvailable.")

        def walk_right():
            msg.showerror(title="Null Action", message="This action is still unvailable.")

        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label="Idle", command=idle)
        self.menu.add_command(label="Idle to Sleep", command=idle_to_sleep)
        self.menu.add_command(label="Sleep", command=sleep)
        self.menu.add_command(label="Sleep to Idle", command=sleep_to_idle)
        self.menu.add_command(label="Walking Towards Left", command=walk_left)
        self.menu.add_command(label="Walking Towards Right", command=walk_right)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.quit)

        # actions declaration
        self.action_name_list = ['idle', 'from idle to sleep', 'walking towards left', 'walking towards right', 'sleep',
                                 'from sleep to idle']
        idle_index = [1, 2, 3, 4]
        idle_to_sleep_index = [5]
        walking_left_index = [6, 7]
        walking_right_index = [8, 9]
        sleep_index = [10, 11, 12, 13, 15]
        sleep_to_idle_index = [14]
        self.action_index = [idle_index, idle_to_sleep_index, walking_left_index, walking_right_index, sleep_index,
                             sleep_to_idle_index]
        idle = [tk.PhotoImage(file=path + 'idle.gif', format='gif -index %i' % i) for i in range(5)]
        idle_to_sleep = [tk.PhotoImage(file=path + 'idle_to_sleep.gif', format='gif -index %i' % i) for i in range(8)]
        walk_positive = [tk.PhotoImage(file=path + 'walking_positive.gif', format='gif -index %i' % i) for i in
                         range(8)]
        walk_negative = [tk.PhotoImage(file=path + 'walking_negative.gif', format='gif -index %i' % i) for i in
                         range(8)]
        sleep = [tk.PhotoImage(file=path + 'sleep.gif', format='gif -index %i' % i) for i in range(3)]
        sleep_to_idle = [tk.PhotoImage(file=path + 'sleep_to_idle.gif', format='gif -index %i' % i) for i in range(8)]
        self.gif_list = [idle, idle_to_sleep, walk_positive, walk_negative, sleep, sleep_to_idle]

        # start
        self.geometry('100x100+' + str(self.x) + '+' + str(self.y))
        # '100x100' = image size
        # x = image position
        # y = floor position
        self.config(highlightbackground='black')
        self.label = tk.Label(self, bd=0, bg='black')
        self.overrideredirect(True)
        self.wm_attributes('-transparentcolor', 'black')
        self.label.pack()
        self.after(1, self.update)
        # random.randrange(1000, 5000, 1000)
        # another event will continue after 1 ~ 5 second(s)

    # make the gif work by loop each frame
    def gif_work(self, frames, first_num, last_num):
        if self.cycle < len(frames) - 1:
            self.cycle += 1
        else:
            self.cycle = 0
            self.event_number = random.randrange(first_num, last_num + 1, 1)
        return self.cycle, self.event_number

    # transfer random no. to event
    def event(self):
        # event number = 1, 2, 3, 4 -> idle
        # event number = 5 -> from idle to sleep
        # event number = 6, 7 -> walking towards left
        # event number = 8, 9 -> walking towards right
        # event number = 10, 11, 12, 13, 15 -> sleep
        # event number = 14 -> from sleep to idle
        for i in range(6):
            if self.event_number in self.action_index[i]:
                self.check = i
                print(self.action_name_list[i])
                self.after(100, self.update)

    # update the frame
    def update(self):
        first_num = 0
        last_num = 0
        frames = self.gif_list[self.check][self.cycle]
        if self.check == 0:  # idle
            # after idle will randomly -> idle / from idle to sleep / walking towards left / walking towards right
            first_num = 1
            last_num = 9
        elif self.check == 1:  # from idle to sleep
            # after from idle to sleep will only -> sleep
            first_num = 10
            last_num = 10
        elif self.check == 2:  # walking towards left
            # after walking towards left will randomly -> idle / from idle to sleep / walking towards left /
            #                                             walking towards right
            first_num = 1
            last_num = 9
            if self.x != 0:
                self.x -= 3
        elif self.check == 3:  # walking towards right
            # after walking towards right will randomly -> idle / from idle to sleep / walking towards left /
            #                                              walking towards right
            first_num = 1
            last_num = 9
            if self.x != self.winfo_screenwidth() - 100:
                self.x += 3
        elif self.check == 4:  # sleep
            # after sleep will randomly -> sleep / from sleep to idle
            first_num = 10
            last_num = 15
        elif self.check == 5:  # from sleep to idle
            # after from sleep to idle will only -> idle
            first_num = 1
            last_num = 1
        self.cycle, self.event_number = self.gif_work(self.gif_list[self.check], first_num, last_num)
        self.geometry('100x100+' + str(self.x) + '+' + str(self.y))
        self.label.configure(image=frames)
        self.after(1, self.event)

        def popup_menu(e):
            self.menu.tk_popup(e.x_root, e.y_root)

        self.bind("<Button-3>", popup_menu)


if __name__ == "__main__":
    cat = Cat()
    cat.mainloop()
