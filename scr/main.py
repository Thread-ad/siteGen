from textnode import TextType, TextNode
import os, shutil


def main():
        
    def public_move(directory,destination):
        if directory == "":
            return

        if os.path.exists(destination):
            shutil.rmtree(destination)
        os.mkdir(destination)

        paths = os.listdir(directory)
      

        for path in paths:
            print(f"path is: {path}")
            print(f"     path is file: {os.path.isfile(path)}")
            if os.path.isfile(path) == True:
                new_dest = os.path.join("public",path)
                print(f"New destination is {new_dest}")
                if os.path.exists(new_dest) != True:
                    os.mkdir(new_dest)
                public_move(os.path.join(directory, path),new_dest)

                
            else :
                shutil.copy(os.path.join(directory,path),destination)


        
        return 

    return public_move("static","public")


    


if __name__ == "__main__":
    main()
