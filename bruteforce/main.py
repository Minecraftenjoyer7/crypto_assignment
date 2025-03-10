import tkinter as t

def bruteforce():
    text = text_input.get()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    y = text.lower()
    z = []
    i = 0
    file_name = "info.txt"
    for shift in range(0,26):
        for l in range(0, 26):
            z.insert(l, alphabet[(l - shift) % 26])

        k = ""
        for m in range(0, len(y)):
            if y[m] in alphabet:
                p = alphabet.index(y[m])
                k += z[p]
            else:
                k += y[m]
        with open(file_name,mode="a") as file:
            if i == 0:
                file.write(f"\nword getting bruteforced: {k}\n"
                           f"------------------------------------------------------------------\n")
            else:
                file.write(f"{i}-{k}\n")
            i+=1
    output_input.config(state="normal")
    output_input.delete(0, t.END)
    output_input.insert(0, f"output saved in {file_name}")
    output_input.config(state="disabled")



#---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("password manager")

#===========================================================================
#image
canvas = t.Canvas(width=200,height=200)
photo = t.PhotoImage(file="logo.png")
#---------------
canvas.create_image(100,100,image = photo)
canvas.grid(row = 0,column = 1)
#===========================================================================
#labels
text_label = t.Label(text="text: ")
text_label.grid(row = 1,column = 0)
#---------------
#===========================================================================
#inputs
text_input = t.Entry(width = 33)
text_input.grid(row = 1,column = 1)
text_input.focus()
#---------------
output_input = t.Entry(width = 40,state="disabled")
output_input.grid(row = 2,column = 1,columnspan = 2)
#---------------
#===========================================================================
#---------------
cipher_button = t.Button(text = "Brute force",width=44,command = bruteforce)
cipher_button.grid(row = 4,column = 1,columnspan = 2)
#---------------
#===========================================================================

window.mainloop()