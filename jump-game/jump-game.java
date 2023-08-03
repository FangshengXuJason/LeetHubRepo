class Solution {
    public boolean canJump(int[] nums) {
        int last_good_index = nums.length-1;
        
        for(int i=nums.length-1;i>=0;i--){
            if(i+nums[i]>=last_good_index){
                last_good_index = i;
            }
        }
        return last_good_index == 0;
    }
}