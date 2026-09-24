class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> container = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++)
        {
            if (!container.containsKey(nums[i]))
            {
                container.put(nums[i], 1);
            }
            else 
            {
                container.put(nums[i], container.get(nums[i]++));
                return true; 
            }
        }

        return false;
    }
}

