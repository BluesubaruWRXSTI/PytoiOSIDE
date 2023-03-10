//
//  CodableFont.swift
//  Pyto
//
//  Created by Emma Labbé on 30-07-20.
//  Copyright © 2018-2021 Emma Labbé. All rights reserved.
//

import UIKit

struct CodableFont: Codable {
    
    var descriptorData: Data
    
    var size: Float
    
    init?(font: UIFont) {
        do {
            descriptorData = try NSKeyedArchiver.archivedData(withRootObject: font.fontDescriptor, requiringSecureCoding: false)
            size = Float(font.pointSize)
        } catch {
            print(error.localizedDescription)
            return nil
        }
    }
    
    var uiFont: UIFont {
        
        #if os(iOS)
        let system = UIFont.systemFont(ofSize: UIFont.systemFontSize)
        #elseif os(watchOS)
        let system = UIFont.systemFont(ofSize: 17)
        #endif
        
        do {
            guard let descriptor = try NSKeyedUnarchiver.unarchivedObject(ofClass: UIFontDescriptor.self, from: descriptorData) else {
                return system
            }
            
            return UIFont(descriptor: descriptor, size: CGFloat(size))
        } catch {
            print(error.localizedDescription)
            return system
        }
    }
}
