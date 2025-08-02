class MyExceptions(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message  # Fix: set self.message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
    
def main():
    a = 0
    try:
        if a == 0:
            raise MyExceptions("Division by zero is not allowed", 400)
    except MyExceptions as e:
        print(e)

main()