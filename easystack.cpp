#include <iostream>
#include <vector>
#include <string>

void readings(int testCases, std::vector<std::string>& myStack);

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;
    std::vector<std::string> myStack;
    readings(t, myStack);
    return 0;
}

void readings(int testCases, std::vector<std::string>& myStack) {
    while (testCases >= 1) {
        std::string input;
        std::cin >> input;
        if (input == "2" && !myStack.empty()) {
            myStack.pop_back();
        } else if (input == "3") {
            if (myStack.empty()) {
                std::cout << "Empty!" << '\n';
            } else {
                std::cout << myStack.back() << '\n';
            }
        } else if (input == "1") {
            std::string number;
            std::cin >> number;
            myStack.push_back(number);
        }
        testCases -= 1;
    }
}
