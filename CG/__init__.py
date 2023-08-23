import cv2
from ffpyplayer.player import MediaPlayer


def PlayVideo():
    # 导入视频文件
    video_path = "video/CG_TEST1.avi"
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    # cv播放视频的操作
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            # audio
            img, t = audio_frame
            # print(img, t)
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    PlayVideo()
