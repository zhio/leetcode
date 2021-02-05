/*
 * @lc app=leetcode.cn id=39 lang=golang
 *
 * [39] 组合总和
 */

// @lc code=start
import "sort"
func combinationSum(candidates []int, target int) [][]int {
	if len(candidates) == 0{
		return [][]int {}
	}

	c,res := []int{}, [][]int{}

	sort.Ints(candidates)
	findcombinationsSum(candidates,target,0,c,&res)
	return res
}

func findcombinationsSum(nums []int,target,index int,c []int, res *[][]int){
	if target <= 0 {
		if target == 0{
			b := make([]int,len(c))
			copy(b,c)
			*res = append(*res,b)
		}
		return 
	}
	for i := index; i< len(nums); i++{
		if nums[i] > target{
			break
		}
		c = append(c,nums[i])
		findcombinationsSum(nums,target-nums[i],i,c,res)
		c = c[:len(c)-1]
	}
}
// @lc code=end

