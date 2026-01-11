class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string mergedString;
        if (word1.size() > word2.size()){
            for (int i = 0; i < word2.size(); i++){
                mergedString += word1[i];
                mergedString += word2[i];
            }
            string slice = word1.substr(word2.size());
            mergedString += slice;
        }
        else if(word1.size() < word2.size()){
            for (int i = 0; i < word1.size(); i++){
                mergedString += word1[i];
                mergedString += word2[i];
            }
            string slice = word2.substr(word1.size());
            mergedString += slice;
        }
        else{
            for (int i = 0; i < word1.size(); i++){
                mergedString += word1[i];
                mergedString += word2[i];
            }
        }
        return mergedString;
    }
};
