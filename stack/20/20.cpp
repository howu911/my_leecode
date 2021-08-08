/*
 * @Description: 20 有效的括号
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-08-08 16:15:01
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-08-08 16:31:07
 */
class Solution {
public:
    bool isEqul(char a, char b) {
        if(b == '{') {
            if(a == '}')  return true;  else  return   false;
        }else if(b == '[') {
            if(a == ']')  return true;  else  return   false;
        }else{
            if(a == ')')  return true;  else  return   false;
        }
    }

    bool isValid(string s) {
        stack<int> stack;
        if(s.size() == 0) {
            return true;
        }
        

        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '{' || s[i] == '[' || s[i] == '(') {
                stack.push(s[i]);
            }
            else {
                if(stack.empty()) {
                    return false;
                }

                if(isEqul(s[i], stack.top())) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }

        if(stack.empty()) {
            return true;
        } else {
            return false;
        }
    }
};

