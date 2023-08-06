#include <iostream>
#include <vector>

using namespace std;

vector<string> find_lcs(const string &file_1, const string &file_2)
{
    vector<string> differences;

    int f1_size = file_1.size();
    int f2_size = file_2.size();
    cout << endl
         << f1_size << '\t' << f2_size << endl;

    vector<vector<int>> lcs_matrix(f1_size + 1, vector<int>(f2_size + 1, 0));

    for (int i = 1; i <= f1_size; i++)
    {
        for (int j = 1; j <= f2_size; j++)
        {
            if (file_1[i - 1] == file_2[j - 1])
            {
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1;
            }
            else
            {
                lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1]);
            }
        }
    }

    cout << " ";
    for (int i = 0; i < f2_size; i++)
    {
        cout << file_2[i] << " ";
    }
    cout << endl;
    for (int i = 1; i < f1_size + 1; i++)
    {
        cout << file_1[i - 1] << " ";
        for (int j = 1; j < f2_size + 1; j++)
        {
            cout << lcs_matrix[i][j] << " ";
        }
        cout << endl;
    }

    int i = f1_size, j = f2_size;

    while (i > 0 && j > 0)
    {
        if (file_1[i - 1] == file_2[j - 1])
        {
            --i;
            --j;
        }
        else
        {
            if (lcs_matrix[i - 1][j] >= lcs_matrix[i][j - 1])
            {
                differences.push_back("- " + file_1.substr(i - 1, 1));
                --i;
            }
            else
            {
                differences.push_back("+ " + file_2.substr(j - 1, 1));
                --j;
            }
        }
    }

    while (i > 0)
    {
        differences.push_back("- " + file_1.substr(i - 1, 1));
        --i;
    }

    while (j > 0)
    {
        differences.push_back("+ " + file_2.substr(j - 1, 1));
        --j;
    }
    //  std::reverse(differences.begin(), differences.end());/

    return differences;
}

int main()
{
    string file_1 = "qwerty rieofr";
    string file_2 = "wert fwrier";
    cout << file_1 << endl
         << file_2;

    vector<string> differences = find_lcs(file_1, file_2);
    // cout << differences;
    for (const std::string &diff : differences)
    {
        std::cout << diff << '\n';
    }

    return 0;
}