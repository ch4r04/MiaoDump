//
//  ViewController.m
//  MytestApp
//
//  Created by ch4r0n on 2018/3/2.
//  Copyright © 2018年 ele.me. All rights reserved.
//

#import "ViewController.h"
#import <UISFrameworkIOS/ELMWBRequestHelper.h>
#import <AFNetworking.h>


#define TICK   NSDate *startTime = [NSDate date]
#define TOCK   NSLog(@"Time: %fms", -[startTime timeIntervalSinceNow] * 1000)

@interface ViewController ()
@property (nonatomic,strong) AFHTTPSessionManager *manager;

@end

@implementation ViewController

- (AFHTTPSessionManager *)manager{
    if (!_manager) {
        self.manager = [AFHTTPSessionManager manager];
    }
    return _manager;
}

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    self.view.backgroundColor = [UIColor blueColor];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event{


    

    
}

- (void)testTime{

}

- (void)testPost{

    
}
@end
