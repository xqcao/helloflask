def currect_id

pipeline{
    agent any
    stages{
        stage("1st task"){
            steps{
                echo "========executing first stage create commitflask.json file========"
                script{
                    currect_id= sh 'git rev-parse HEAD'
                    echo "currect id is ${currect_id}"
                    def _ids =  getCommitIds()

                    for(int j=0;j<_ids.size();j++){
                        try {
                            echo "this is try block"
                        } catch (Exception e) {
                            echo 'Handle the exception!'
                        }
                        echo "commit id: ${_ids[j]}"
                    }
                }
            } 
        }
        stage("2nd task"){
            steps{
                echo "=====run python to generate version-json file"
                script{
                    def pys = dopy_process()
                    echo "2nd-return-value: ${pys}"
                }
            }
        }
        stage("")

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

def dopy_process(){
    sh "python3 do_version.py"
    def data2=readJSON file: "allv.json"
    echo "json_data: ${data2}"
    return "all json job is done"
}

def getVersionTage(String id){
    def data3=readJSON file: "allv.json"
    return data3[id]
}
