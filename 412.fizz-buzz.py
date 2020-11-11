#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        fizee_buzz_dict = {3:"Fizz",5:"Buzz"}

        for num in range(1,n+1):
            num_ans_str = ""
            for key in fizee_buzz_dict.keys():
                if num % key == 0:
                    num_ans_str += fizee_buzz_dict[key]
            
            if not num_ans_str:
                num_ans_str = str(num)
            
            ans.append(num_ans_str)
        return ans
        
# @lc code=end

