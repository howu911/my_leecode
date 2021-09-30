/*
 * @Description: 167. 两数之和 II - 输入有序数组
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-09-10 23:13:28
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-09-10 23:28:04
 */

package main

import "fmt"

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}

func twoSum(numbers []int, target int) []int {
	start, end := 0, len(numbers)-1
	for start < end {
		if numbers[start]+numbers[end] < target {
			start++
		} else if numbers[start]+numbers[end] > target {
			end--
		} else {
			return []int{start + 1, end + 1}
		}
	}
	return nil
}
