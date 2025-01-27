# NBA Shot Prediction: Model Development and Evaluation

## Introduction.
This study aims to develop a predictive model for determining the success of NBA shots using features like shot distance, defender proximity, and shot clock time. The dataset, sourced from Kaggle (https://www.kaggle.com/datasets/dansbecker/nba-shot-logs, 128k shots), was preprocessed to encode variables numerically and scaled to [-1,1]. Shooter and defender IDs were target-encoded.

## Related Work.
A project from Stanford CS229 by Brett Meehan inspired this study (https://cs229.stanford.edu/proj2017/final-reports/5132133.pdf). The prior work explored various models, including logistic regression, support vector machines (SVM), neural networks, Naïve Bayes, random forests, and boosting. Boosting achieved the highest accuracy (~68%), while neural networks performed poorly (~55%). This project aimed to improve neural network performance and deepen insights into the dataset.

## Methodology.
- **Logistic Regression**: Established baseline performance.
- **Neural Networks**: Models were trained with He initialization and evaluated using 10-fold cross-validation and a test set (5% split). Threshold optimization via Youden's J statistic improved accuracy by ~1.5%.  
- **Feature Importance**: Logistic regression was used to evaluate variable contributions by training models with only individual variables.  

## Results.
### **Logistic Regression**

Training models with only individual variables yielded the following results. The individual varaibles that created the best performing models were shot distance, closest defender id, and shooter id. Models with ~0.5 AUC or lower which should be seen as random guessing or worse were excluded. Models excluded used the following variables: location (home/away), win/loss, the number of shots taken before the current one, the amount of time spent with the ball before shooting it, and the distance to the closest defender.

<img src="https://github.com/user-attachments/assets/bd5c3f80-62be-4193-9d68-9189d1bd2199" alt="features" width="600">

A model trained on all 13 variables obtained the following performance.
   - Cross-validation: Accuracy = 61.6%, AUC = 63.5%
   - Test set: Accuracy = 60.9%, AUC = 62.9%.

<img src="https://github.com/user-attachments/assets/59884068-d062-4683-b175-fd62f74bbc69" alt="features" width="600">

This is roughly in line with what was achieved in the project by Meehan. Surprisingly, the model trained solely on shot distance performed only slightly worse.

### **Neural Networks**

Grid searching for the number of hidden layers and the number of neurons in each layer yielded the following heatmaps.

<img src="https://github.com/user-attachments/assets/7fbda5a7-2983-456a-9b66-7e6c42acde3e" alt="features" width="600">
<img src="https://github.com/user-attachments/assets/a1c84a3e-5420-4e6a-91ac-4157cb29b9fc" alt="features" width="600">

Some of my conclusions from the heatmaps:
   - Models generally performed better with more neurons but the performace increased only marginally after ~32.
   - Larger neuron counts definitely reduced variance in model performance.
A single hidden layer with 256 neurons achieved the following results:
   - Cross-validation: Accuracy = 62.9%, AUC = 65.2%
   - Test set: Accuracy = 64.4%, AUC = 66.0%.

<img src="https://github.com/user-attachments/assets/c61bf45c-ee80-4c75-8cde-1693d30b95bc" alt="features" width="600">

Though this was much better than what was achieved in the project by Meehan, it still underperformed compared to boosting.

## Findings/Conclusions.
- Surprisingly, the distance to the closest defender didn't seem to have strong (surface-level) predictive power.  
- Training a logistic regression model on shot distance alone outperformed Meehan's neural network.
- Even a complex neural network performed only a few percentage points (~4%) better than a simple logistic regression model trained solely on a variable like shot distance, player id, or closest defender id.
- The neural networks didn't seem like they were taking full advantage of the dataset's predictive power.
- AUC was a more reliable evaluation metric than accuracy as its variance was slightly lower.
- Utilizing optimal thresholds with Youden's J statistic improved model performance more than increasing complexity.
