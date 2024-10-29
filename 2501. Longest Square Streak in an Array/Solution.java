class Solution {
    public int longestSquareStreak(int[] nums) {
        int currentStreak;
        int longestStreak = 0;
        var unique = new HashSet<Integer>();
        Arrays.sort(nums);
        for(int n :  nums){
            unique.add(n);
        }
        for (int n : nums) {
            long current = n;
            currentStreak = 0;
            while(unique.contains( (int) current)){
                currentStreak ++;
                if (current * current > 1e5) break;
                current = current * current;
            }
            longestStreak = Math.max(longestStreak, currentStreak);
        }
        return longestStreak >= 2 ? longestStreak : -1;
    }
}