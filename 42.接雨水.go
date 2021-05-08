/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */

// @lc code=start
func trap(height []int) int {
	res,left,right,maxLeft,maxRigth := 0,0,len(height)-1,0,0
	for left<=right{
		if height[left] < height[right]{
			if height[left]>maxLeft{
				maxLeft = height[left]
			}else{
				res += maxLeft - height[left]
			}
			left ++
		}else{
			if height[right]>= maxRigth{
				maxRigth = height[right]
			}else{
				res += maxRigth - height[right]
			}
			right --
		}
	}
	return res
}
// @lc code=end

