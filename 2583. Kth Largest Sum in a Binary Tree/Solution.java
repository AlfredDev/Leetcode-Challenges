//  https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/?envType=daily-question&envId=2024-10-22
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
public class Solution {
    public long kthLargestLevelSum(TreeNode root, int k) {
        Queue<TreeNode> cola = new LinkedList<>();
        var levelSum = new ArrayList<Long>();
        cola.add(root);
        while (!cola.isEmpty()) {
            int size = cola.size();
            long sum = 0;
            for (int i = 0; i < size; i++) {
                var node = cola.poll();
                sum += node.val;
                if (node.left != null)
                    cola.add(node.left);
                if (node.right != null)
                    cola.add(node.right);
            }
            levelSum.add(sum);
        }
        levelSum.sort(Collections.reverseOrder());
        if (k <= levelSum.size())
            return levelSum.get(k - 1);
        return -1;
    }
}
