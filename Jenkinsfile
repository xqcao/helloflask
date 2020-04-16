def flag
pipeline{
    agent any
    environment{
        current_id= sh script: 'git rev-parse HEAD', returnStdout: true
    }
    stages{
        stage("1st task"){
            steps{
                echo "========executing first stage create commitflask.json file========"
                script{
                    
                    echo "currect id is ${current_id}"
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
        stage("3rd task"){
            steps{
                echo "check image is exist?"
                script{
                    withCredentials([string(credentialsId: 'docker-hub-pwd', variable: 'dockerHubPwd')]) {
                            sh "docker login -u adamcao -p ${dockerHubPwd}"           
                            def img = "nginx:1.15.8"
                            def isImageexist = sh script: "docker images -q ${img}", returnStdout: true
                            echo "${img} is ${isImageexist}"
                            if(isImageexist !=""){
                                flag=false
                            }else{
                                flag=true
                            }

                            // def img2 = "nginx:1.15.8"
                            // def isImageexist2 = sh script: "docker images -q ${img2}", returnStdout: true
                            // echo "${img2} is ${isImageexist2}"
                            
                    }
                }
            }
        }
        stage("4th task"){
            steps{
                script{
                    if(flag){
                        echo "start build images"
                    }else{
                        echo "image existed, skip image build ...."
                    }
                 }
            }
        }
        stage("5th task"){
            when { flag }
            steps{
                echo "when flag is true, this 5th task is run, current_flag: ${flag}, do this"
            }
        }
         stage("6th task"){
            when { not flag }
            steps{
                echo "when flag is false, this 6th task is run, current_flag: ${flag}, do this"
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
