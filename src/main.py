import chem_lex.ChemlabLexer as Lexer
import chem_parse.ChemlabParser as Parser
import sys


def main():
    # If no file name passed when running we open the ChemLAB command line, if not we try to parse the file passed
    try:
        # Check if something was passed. If not, we open command line theme
        trace = False
        lexer = Lexer.ChemLABLexer()
        lexer.build()
        parser = Parser.ChemlabParser()
        parser.build(trace=trace)
        if len(sys.argv) <= 1:
            while True:
                try:
                    buff = input("ChemLAB >>")
                    if not buff:
                        continue
                    if trace:
                        print("Buffer Content: ")
                        print(buff)
                        print("Tokenized buffer: ")
                        lexer.test(buff)
                        print("Parsing File...")
                    parser.parseContent(buff, lexer.lexer)
                except KeyboardInterrupt:
                    exit()
                except Exception as e:
                    print("Error on line `"+ buff +"`\nPlease try again")
                    print("Error was: "+str(e))
                    continue
        else:
            filename = sys.argv[1]
            if trace:
                print("Prepping to parse file "+filename)
            file = open(filename, 'r')
            s = file.read()
            if trace:
                print("File Content: ")
                print(s)
                print("Tokenized file: ")
                lexer.test(s)
                print("Parsing File...")
            parser.parseContent(s, lexer.lexer)
    except (FileNotFoundError, EOFError) as e:
        print("Error reading file. Could not open or read.\n")
    except Exception as e2:
        print("Error parsing content. Could not parse file.\n")
        print("Error found: "+str(e2))
    finally:
        try:
            file.close()
        except NameError:
            pass



if __name__ == "__main__":
    main()