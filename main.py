"""
*This Program is wriiten for The minimal management of media to listen, read and watch.
*The program allows the user to add, delete and list the media to listen, read and watch.
*The program allows the user to add a reflection of the media listened, read and watched.
"""

class Media():
    
    def music_tolisten() -> str:
        try:
            with open('music.txt', 'r') as f:
                return f'''-- MUSIC TO LISTEN --
                {f.read()} '''
        except Exception as e:
            return f'Error: {e}\n Try again'    
        
    def add_to_listen() -> None:
        while True:
            music = input('Enter the music to listen(Enter "q" to exit): ')
            try:
                if music == 'q':
                    break
                else:
                    with open('music.txt', 'a') as f:
                        f.write(music + '\n')
                
            except Exception as e:
                print(f'Error: {e}\n Try again')

    def to_delete_music() -> str:
        while True:
            to_delete = input('Enter the music to delete: ')
            to_delete = to_delete.strip()
            if to_delete == 'q':
                break
            else:
                try:
                    with open('music.txt', 'r') as f:
                        lines = f.readlines()
                        
                        with open('music.txt', 'w') as fw:
                            for line in lines:
                                if line.strip() != to_delete:
                                    fw.write(line)
                    with open('music.txt', 'r') as f:
                        return f.read()
                    return f'deleted {to_delete}'
                except Exception as e:
                    return f'Error: {e}\n Try again'
                
    def books_toread() -> str:
        try:
            with open('books.txt', 'r') as f:
                a = f.read()
                return f'''-- BOOKS TO READ --
                                {a} '''
        except Exception as e:
            return f'Error: {e}\n Try again'
        
    def add_to_read() -> None:
        while True:
            book = input('Enter the book to read(enter "q" to exit): ')
            try:
                if book == 'q':
                    break
                else:
                    with open('books.txt', 'a') as f:
                        f.write(book + '\n')

            except Exception as e:
                print(f'Error: {e}\n Try again')

    def to_delete_book() -> str:
        while True:
            to_delete = input('Enter the book to delete("q" to exit): ')
            to_delete = to_delete.strip()
            if to_delete == 'q':
                break
            else:
                try:
                    with open('books.txt', 'r') as f:
                        lines = f.readlines()
                        
                        with open('books.txt', 'w') as fw:
                            for line in lines:
                                if line.strip() != to_delete:
                                    fw.write(line)
                    with open('books.txt', 'r') as f:
                        return f.read()
                    return f'deleted {to_delete}'
                except Exception as e:
                    return f'Error: {e}\n Try again'
                
    def movies_towatch() -> str:
        try:
            with open('movies.txt', 'r') as f:
                return f'''-- MOVIES TO WATCH --
                                {f.read()} '''
        except Exception as e:
            return f'Error: {e}\n Try again'
        
    def add_to_watch() -> None:
        while True:
            movie = input('Enter the movie to watch(enter "q" to exit): ')
            if movie == 'q':
                break
            else:
                try:
                    with open('movies.txt', 'a') as f:
                        f.write(movie + '\n')
                except Exception as e:
                    print(f'Error: {e}\n Try again')

    def to_delete_movie() -> str:
        while True:
            to_delete = input('Enter the movie to delete("q" to exit): ')
            to_delete = to_delete.strip()
            if to_delete == 'q':
                break
            else:
                try:
                    with open('movies.txt', 'r') as f:
                        lines = f.readlines()
                        
                        with open('movies.txt', 'w') as fw:
                            for line in lines:
                                if line.strip() != to_delete:
                                    fw.write(line)
                    with open('movies.txt', 'r') as f:
                        return f.read()
                    return f'deleted {to_delete}'
                except Exception as e:
                    return f'Error: {e}\n Try again'
        
    def music_listened() -> str:
        music1 = input('Enter the music listened: ')
        music_reflection = input('Add a short reflection of the music: ')
        try:
            with open('music_listened.txt', 'a') as f:
                f.write(f'{music1} - {music_reflection}\n')
        except Exception as e:
            print(f'Error: {e}\n Try again')

    def books_read() -> str:
        book1 = input('Enter the book read: ')
        book_reflection = input('Add a short reflection of the book: ')
        try:
            with open('books_read.txt', 'a') as f:
                f.write(f'{book1} - {book_reflection}\n')
        except Exception as e:
            print(f'Error: {e}\n Try again')

    def movies_watched() -> str:
        movie1 = input('Enter the movie watched: ')
        movie_reflection = input('Add a short reflection of the movie: ')
        try:
            with open('movies_watched.txt', 'a') as f:
                f.write(f'{movie1} - {movie_reflection}\n')
        except Exception as e:
            print(f'Error: {e}\n Try again')

    def music_menu() -> None:
        
        print('''-- MUSIC --''')
        print('''
                1. Music to listen
                2. Add music to listen
                3. Delete music
                4. Music listened
                q. Quit''')
                
        option = input('Enter the option: ')
        if option == '1':
            print(Media.music_tolisten())
            
        elif option == '2':
            Media.add_to_listen()
        elif option == '3':
            print(Media.to_delete_music())
        elif option == '4':
            Media.music_listened()
        elif option == 'q':
            print("goodbye :)")
            
        else:
            print('Invalid option. Try again')

    def books_menu() -> None:
        
        
        print('''
                -- BOOKS --
                1. Books to read
                2. Add book to read
                3. Delete book
                4. Books read
                q. Quit''')
                
        option = input('Enter the option: ')
        if option == '1':
            print(Media.books_toread())
            
        elif option == '2':
            Media.add_to_read()
        elif option == '3':
            print(Media.to_delete_book())
        elif option == '4':
            Media.books_read()
        elif option == 'q':
            print("goodbye :)")
            
        else:
            print('Invalid option. Try again')  
                
    def movies_menu() -> None:
        
        print('''
                -- MOVIES --
                1. Movies to watch
                2. Add movie to watch
                3. Delete movie
                4. Movies watched
                q. Quit''')
                
        option = input('Enter the option: ')
        if option == '1':
            print(Media.movies_towatch())
            
        elif option == '2':
            Media.add_to_watch()
        elif option == '3':
            print(Media.to_delete_movie())
        elif option == '4':
            Media.movies_watched()
        elif option == 'q':
            print("goodbye :)")
            
        else:
            print('Invalid option. Try again')

    def main_menu() -> None:
        # print('''''')
        print('''
                    -- MEDIA --
                    1. Music
                    2. Books
                    3. Movies
                    q. Quit''')
                
        option = input('Enter the option: ')
        if option == '1':
            Media.music_menu()
        elif option == '2':
            Media.books_menu()
        elif option == '3':
            Media.movies_menu()
        elif option == 'q':
            print("goodbye :)")
        
        else:
            print('Invalid option. Try again')
def main() -> None:
    Media.main_menu()
    

if __name__ == '__main__':
    main()
    
