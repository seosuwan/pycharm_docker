import numpy as np
import pandas as pd
from titanic.model.dataset import Dataset
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier


'''
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
'''

class TitanicService(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        return pd.read_csv(f"/data/{payload}.csv")

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)
    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']
    @staticmethod
    def drop_feature(this, *feature) -> object: #필요없는 데이터 제거
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.train.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1,'C': 2,'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this
    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1,2,3,4})
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4,labels={1,2,3,4})
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['Fare'] = this.train['Fare'].fillna(1)
        # Qcut을 사용하면 자동으로 구간을 4등분한다.
        # 타이타닉에서는 bins = [-1 , 8, 15, 31, np.inf]
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6,
                       'Senior': 7}
        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train,this.test]
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset["Title"] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer','Dona','Mme'],'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle','Mr')
            dataset['Title'] = dataset['Title'].replace('Ms','Miss')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this



    @staticmethod
    def gender_nominal(this)-> object:
        combine = [this.train, this.test]
        sex_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset["Gender"] = dataset['Sex'].map(sex_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)


    def accuracy_by_classfier(self, this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=self.create_k_fold(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) *100, 2 )


