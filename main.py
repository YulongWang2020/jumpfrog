import pybullet as p
import time
import pybullet_data



if __name__ == '__main__':
    print("helloword")
    physicsClient= p.connect(p.GUI)#or p.DIRECTfor non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
    p.setGravity(0,0,-10)
    planeId= p.loadURDF("plane.urdf")
    cubeStartPos= [0,0,0.27]
    cubeStartOrientation= p.getQuaternionFromEuler([0,0,0])
    boxId= p.loadURDF("C:/Users\Lorne\PycharmProjects\Simulation\jumpfrog.urdf",cubeStartPos, cubeStartOrientation)
    for i in range(15):
        print("--------------", p.getJointInfo(boxId, i))
    for i in range(15):
        print("--------------",i,"::", p.getEulerFromQuaternion(p.getLinkState(boxId, i)[1]))
        print("--------------", i, "::", p.getJointState(boxId, i))

    # p.setJointMotorControl2(boxId, 3, p.POSITION_CONTROL, -0.6)
    # print(p.getEulerFromQuaternion(p.getLinkState(boxId, 5)[1]))
    # p.setJointMotorControl2(boxId, 10, p.POSITION_CONTROL, 4)
    p.setJointMotorControl2(boxId, 7, p.POSITION_CONTROL, 2)
    p.setJointMotorControl2(boxId, 14, p.POSITION_CONTROL, 2)
    p.setJointMotorControl2(boxId, 3, p.POSITION_CONTROL, -1)
    p.setJointMotorControl2(boxId, 10, p.POSITION_CONTROL, -1)
    p.setJointMotorControl2(boxId, 2, p.POSITION_CONTROL, 0.35)
    p.setJointMotorControl2(boxId, 9, p.POSITION_CONTROL, 0.35)
    p.setJointMotorControl2(boxId, 6, p.POSITION_CONTROL, -0.5)
    p.setJointMotorControl2(boxId, 13, p.POSITION_CONTROL, -0.5)
    # print("--------------", list(p.getLinkState(boxId, 1)[0] + p.getEulerFromQuaternion(p.getLinkState(boxId, 1)[1])))
    # c = p.createConstraint(boxId, 3, boxId, 5, p.JOINT_POINT2POINT, [1, 0, 0], [0, 0, -0.1],[0, 0, 0])
    for i in range (10000):
        p.stepSimulation()
        time.sleep(1./240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1. / 240.)
        p.stepSimulation()
        time.sleep(1./240.)

        # time.sleep(100)



    print("--------------", p.getJointInfo(boxId, 2))
    cubePos, cubeOrn= p.getBasePositionAndOrientation(boxId)
    print(cubePos,cubeOrn)
    print("--------------",p.getJointInfo(boxId,2))
    p.disconnect()