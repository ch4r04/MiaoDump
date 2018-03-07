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

    [self testPost];

    

    
}

- (void)testTime{
    NSString *url = @"http://restapi.ar.elenet.me/newretail/store/v3/150007715?groupId=&latitude=31.23293113708496&longitude=121.3825912475586lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllhttp://restapi.ar.elenet.me/newretail/store/v3/150007715?groupId=&latitude=31.23293113708496&longitude=121.3825912475586lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll";
    
    NSMutableURLRequest *req = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]];
    
    //    NSMutableArray *array = [[NSMutableArray alloc] init];
    //    for (int j = 0; j < 100; j++){
    //        CFAbsoluteTime start = CFAbsoluteTimeGetCurrent();
    //    for (int i = 0; i < 5 ; i++){
    //        [ELMWBRequestHelper atlasSignURLRequestToHeader:req];
    //    }
    //        CFAbsoluteTime end = CFAbsoluteTimeGetCurrent();
    //        [array addObject:[NSNumber numberWithDouble:(end-start) * 1000]];
    //    }
    //    NSLog(@"successful");
    //    __block double sum = 0;
    //    [array enumerateObjectsUsingBlock:^(NSNumber *obj, NSUInteger idx, BOOL * _Nonnull stop) {
    //        sum = sum + obj.doubleValue;
    //    }];
    //
    //
    //    NSLog(@"avg == %f ms",sum / [array count]);
    CFAbsoluteTime start = CFAbsoluteTimeGetCurrent();
    for (int i = 0; i < 5 ; i++){
        [ELMWBRequestHelper atlasSignURLRequestToHeader:req];
    }
    CFAbsoluteTime end = CFAbsoluteTimeGetCurrent();
    NSLog(@"avg == %f ms", end - start);
}

- (void)testPost{
    NSString *url = @"http://10.12.35.128:8195";
    
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]];
    [ELMWBRequestHelper atlasSignURLRequestToHeader:request];
    NSLog(@"%@",[request allHTTPHeaderFields]);
    
    
    NSOperationQueue *queue = [NSOperationQueue currentQueue];
    [NSURLConnection sendAsynchronousRequest:request queue:queue completionHandler:^(NSURLResponse * _Nullable response, NSData * _Nullable data, NSError * _Nullable connectionError) {
        
        NSLog(@"ok");
    }];
    
    
    
}
@end
