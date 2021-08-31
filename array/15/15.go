/*
 * @Description: 15 三数之和 go
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-08-29 22:36:15
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-08-31 23:14:48
 */

package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4})) // [[-1 -1 2] [-1 0 1]]
	fmt.Println(threeSum([]int{-2, 0, 0, 2, 2}))      // [[-2 0 2]]
}

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	var res [][]int

	for i, num := range nums {
		if num > 0 {
			break
		}

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		l, r := i+1, n-1
		for l < r {
			sum := num + nums[l] + nums[r]
			switch {
			case sum > 0:
				r--
			case sum < 0:
				l++
			default:
				res = append(res, []int{num, nums[l], nums[r]})
				// 去除掉重复元素
				for l < r && nums[l] == nums[l+1] {
					l++
				}
				for r > l && nums[r] == nums[r-1] {
					r--
				}

				l++
				r--
			}
		}
	}
	return res
}
