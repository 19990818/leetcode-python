class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        def cond1():
            return len(password)>=8
        def cond2():
            for v in password:
                if v.isdigit():
                    return True
            return False
        def cond3():
            for v in password:
                if v.islower():
                    return True
            return False
        def cond4():
            for v in password:
                if v.isupper():
                    return True
            return False
        def cond5():
            for v in password:
                if v in "!@#$%^&*()-+":
                    return True
            return False
        def cond6():
            for i in range(1,len(password)):
                if password[i]==password[i-1]:
                    return False
            return True
        return cond1() and cond2() and cond3() and cond4() and cond5() and cond6()