pipeline{
    agent{
        label "node"
    }
    stages{
        stage("1st task"){
            steps{
                echo "========executing first stage========"
                script{
                    def _ids =  getCommitIds()
                    for(int j=0;j<_ids.size();j++){
                        echo "commit id: ${_ids[i]}"
                    }
                }
            }
            
        }
    }
    
}

def getCommitIds(){
    sh "curl https://api.github.com/repos/xqcao/helloflask/commits?pre_page=5 > commitflask.json"
    def data = readJSON file: "commitflask.json"
    def ids =new String[data.size()]
    for(int i=0;i<data.size();i++){
        def elements =data[i]['commit']['url'].split('/')
        ids[i]=elements[elements.size()-1]
    }
    return ids

}