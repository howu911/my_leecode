/*
 * 第一次做通过
 * 方法：通过前中后指针的做法
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr)
            return nullptr;

        ListNode* p1 = head;
        ListNode* p2 = head->next;
        ListNode* p3 = nullptr;

        p1->next = nullptr;

        while(p2)
        {
            p3 = p2->next;
            p2->next = p1;
            p1 = p2;
            p2 = p3;
        }
        
        return p1;
    }
};