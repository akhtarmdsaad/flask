import os
print("This is your todo list manager")

todo = []
filename = "todolist.txt"

# For testing purpose
#filename="test.txt"


if os.path.exists(filename):
    print("the file is present")
else:
    print("No such file exist\ncreating a new todo")
    open(filename,"w+")


print("Reading the file")
f = open(filename)
t = f.readline()
while t:
    todo.append(t)
    t=f.readline()
del t

print("Ready!!\n\n")

def _cu(text):
    if text.endswith(">\n"):
        return "completed"
    elif text.endswith("<\n"):
        return "uncompleted"
    else:
        return "error"

def read():
    print("\nYour Todos are:\n")
    for i in range(len(todo)):
        print(i+1,": ",todo[i].replace("<"," ").replace(">"," "),"(",_cu(todo[i]),")\n")

def update():
    print("Updating the list....",end="\r")
    f=open(filename,"w")
    f.truncate()
    f.close()
    del f
    f = open(filename,"a")
    for i in todo:
        if i.endswith("\n"):
            f.write(i)
        else:
            f.write(i+"\n")
    print("Updated                ")
def write(text):
    todo.append(text+"<\n")
    update()
# ">" - completed
# "<" - not completed
def print_pending_todos():
    for j,i in enumerate(todo):
        if i.endswith("<\n"):
            print(j+1,":",i.replace("<"," "),"\n")
def report():
    not_completed = 0
    for i in todo:
        if i.endswith("<\n"):     #not completed
            not_completed+=1
    print("Pending todos: ", not_completed)
    print("Completed todos", len(todo)-not_completed)
    
    if input("Do you want to see pending todos??\n(y/n)>") == "y":
        print_pending_todos()
def remove(no):
    if no>len(todo):
        print("The todo doesn't exist")
    todo.pop(no-1)
def mark_completed(no):
    no-=1
    if todo[no].endswith(">\n"):
        print("Already completed")
        return
    elif todo[no].endswith("<\n"):
        todo[no] = todo[no].replace("<", ">")
    print("marked",no+1,"completed")
    update()
def mark_uncompleted(no):
    no-=1
    if todo[no].endswith("<\n"):
        print("Already uncompleted")
        return
    elif todo[no].endswith(">\n"):
        todo[no] = todo[no].replace(">", "<")
    print("marked",no+1,"uncompleted")
    update()
def clear_all():
    if input("Are you sure to clear all the todos??\n(y/n) >")!="y":
        return
    global todo
    todo=[]
    update()

def help():
    print("""
    read
    add do my homework
    ren(ame) 5
    rep(ort)
    m(ark) c(ompleted) 1(any task no)
    m(ark) u(ncompleted) 1(any task no)
    rem(ove) 1 3 5(any task no)
    pend(ing)
    ch(ange) 1 3
    exit
    
    or directly type the task no. to get the task
    """)
while True:
    user = input(">").lower()
    if user.replace(" ","")=="":
        continue
    try:
        i=int(user)-1
        if i<0:
            raise IndexError
        print(i+1,": ",todo[i].replace("<"," ").replace(">"," "),"(",_cu(todo[i]),")\n")
        continue
    except IndexError:
        print("You have a total of",len(todo),"tasks")
        continue
    except:pass
        
    use = user.strip("\n ").split()
    try:
        if use[0] == "read":
            read()
        elif use[0]=="":
            pass
        elif use[0] == "add" or use[0]=="write":
            write(" ".join(use[1:]))
        elif use[0].startswith("ren"):
            try:
              n=int(use[1])-1
              if n<0:
                raise IndexError
              print("old task:")
              print(todo[n])
              t=input("Rename task(leave blank to cancel):")
              if t=="":
                  continue
              if input("Confirm change?(y/n):").lower()=="y":
                  todo[n]=t+todo[n][-2:]
                  del t
                  update()
              
              
              
            except IndexError:
                print("You have a total of",len(todo),"tasks")
                continue
            except ValueError:
                print("Enter the task no. to change")
                continue
            except Exception as e:print("Except:",e)
            
        elif use[0].startswith("rep"):
            report()
        elif use[0].startswith("m"):
            if use[1].startswith("c"):
                mark_completed(int(use[2]))
            if use[1].startswith("u"):
                mark_uncompleted(int(use[2]))
        elif use[0].startswith("rem"):
            nos=0
            for i in sorted(use[1:]):
                remove(int(i)-nos)
                nos+=1
            update ()
        elif use[0]=="help":
            help()
        elif use[0].startswith("ch"):
            try:
                x=int(use[1])-1
                y=int(use[2])-1
                todo[x],todo[y] = todo[y],todo[x]
                print(f"Changed {x+1} and {y+1}")
                update()
            except ValueError:
                print("Please write those no. to change")
            except:
                print("PLEASE READ HELP")
                help()
        elif use[0].startswith("pend"):
            print_pending_todos()
        elif use[0]=="exit":
            break
        elif use[0]=="clear":
            clear_all()
        else:
            help()
    except Exception as e:
        print(e)
        help()
    
        

