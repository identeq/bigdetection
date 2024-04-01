"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2024-03-27
"""
import time

from big_detection.mmdet.apis.inference import init_detector, inference_detector, show_result_pyplot, init_detector_v1


def image_od_demo():
    # build the model from a config and a checkpoint file
    # config = "/home/dell/Documents/git_repos/bigdetection/big_detection/configs/BigDetection/cbnetv2/htc_cbv2_swin_base_giou_4conv1f_adamw_bigdet.py"
    checkpoint = "/home/dell/Documents/git_repos/bigdetection_model/htc_cbv2_swin_base_giou_4conv1f_bigdet.pth"
    device = "cpu"
    img = "/home/dell/Documents/git_repos/big_detection_test_result/demo_input/demo5.png"
    score_thr = 0.3
    out_file = "/home/dell/Documents/demo5_output.jpg"
    start_time = time.time()
    print("Start time: ", start_time)
    # model = init_detector_v1(config, checkpoint, device=device)
    model = init_detector_v1(checkpoint=checkpoint, device=device)
    # test a single image
    result = inference_detector(model, img)
    print(f"Total time taken: {time.time() - start_time}")
    # show the results
    show_result_pyplot(model, img, result, score_thr=score_thr, out_file=out_file)


if __name__ == '__main__':
    image_od_demo()
