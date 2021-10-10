package main

import (
	"fmt"
	"sort"
)

func merge(intervals [][]int) [][]int {
	if len(intervals) <= 1 {
		return intervals
	}

	res := [][]int{}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for i := 0; i < len(intervals); i++ {
		if len(res) == 0 || res[len(res)-1][1] < intervals[i][0] {
			res = append(res, intervals[i])
		} else {
			res[len(res)-1][1] = max(res[len(res)-1][1], intervals[i][1])
		}
	}

	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := [][]int{{1, 4}, {0, 2}, {3, 5}}
	fmt.Println(merge(a))
}
