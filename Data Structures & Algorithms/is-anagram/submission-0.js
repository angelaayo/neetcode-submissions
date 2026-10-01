class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length){
            return false;
        }
        for(let i=0; i<s.length; i++){
            let found  = false;
            for(let j=0; j<t.length; j++){
                if(s[i] == t[j]){
                    //remove that character from t
                    t = t.slice(0, j) + t.slice(j+1);
                    found = true;
                    break;
                }
            }
            if(!found) return false;
        }
        return true;
    }
}
