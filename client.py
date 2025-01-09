import grpc
from user_management_pb2 import *
from user_management_pb2_grpc import UserManagementStub

def menu():
    print("\nMenu:")
    print("1. Register User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Get Latest Stock Value")
    print("5. Get Average Stock Value")
    print("6. Exit")

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = UserManagementStub(channel)
        while True:
            menu()
            choice = input("Select an option: ")
            if choice == '1':
                email = input("Enter email: ")
                ticker = input("Enter stock ticker: ")
                highvalue =float(input("Enter high value:"))
                lowvalue= float(input("Enter low value:")) 
                telegramid= int(input("Enter telegramid:")) 
                response = stub.RegisterUser(RegisterUserRequest(email=email, ticker=ticker, highvalue=highvalue, lowvalue=lowvalue, telegramid=telegramid))
                print(response.message)
            elif choice == '2':
                email = input("Enter email: ")
                ticker = input("Enter stock ticker: ")
                highvalue =float(input("Enter high value:"))
                lowvalue= float(input("Enter low value:")) 
                telegramid= int(input("Enter telegramid:")) 
                response = stub.UpdateUser(UpdateUserRequest(email=email, ticker=ticker, highvalue=highvalue, lowvalue=lowvalue, telegramid=telegramid))
                print(response.message)
            elif choice == '3':
                email = input("Enter email: ")
                response = stub.DeleteUser(DeleteUserRequest(email=email))
                print(response.message)
            elif choice == '4':
                email = input("Enter email: ")
                response = stub.GetLatestStockValue(GetLatestStockValueRequest(email=email))
                print(f"Ticker: {response.ticker}, Value: {response.value}, Timestamp: {response.timestamp}")
            elif choice == '5':
                email = input("Enter email: ")
                count = int(input("Enter number of recent values to average: "))
                response = stub.GetAverageStockValue(GetAverageStockValueRequest(email=email, count=count))
                print(f"Average Value: {response.average}")
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

